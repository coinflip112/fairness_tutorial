import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

# set layout parameters to avoid cutting off x-axis tick labels
from matplotlib import rcParams

rcParams.update({"figure.autolayout": True})


from sklearn import clone
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.validation import check_is_fitted
from sklearn.exceptions import NotFittedError


# show_proportions is only a helper function for plotting
def show_proportions(
    X, sensitive_features, y_pred, y=None, description=None, plot_row_index=1
):
    plt.figure(plot_row_index, figsize=(10, 6), dpi=340)
    plt.title(description)
    plt.ylabel("P[recidivism predicted | conditions]")

    indices = {}
    positive_indices = {}
    negative_indices = {}
    recidivism_count = {}
    recidivism_pct = {}
    groups = np.unique(sensitive_features.values)
    n_groups = len(groups)
    max_group_length = max([len(group) for group in groups])
    color = cm.rainbow(np.linspace(0, 1, n_groups))
    x_tick_labels_basic = []
    x_tick_labels_by_label = []
    for index, group in enumerate(groups):
        indices[group] = sensitive_features.index[sensitive_features == group]
        recidivism_count[group] = sum(y_pred[indices[group]])
        recidivism_pct[group] = recidivism_count[group] / len(indices[group])
        plt.bar(index + 1, recidivism_pct[group], color=color[index])
        x_tick_labels_basic.append(group)

        if y is not None:
            positive_indices[group] = sensitive_features.index[
                (sensitive_features == group) & (y == 1)
            ]
            negative_indices[group] = sensitive_features.index[
                (sensitive_features == group) & (y == 0)
            ]
            prob_1 = sum(y_pred[positive_indices[group]]) / len(positive_indices[group])
            prob_0 = sum(y_pred[negative_indices[group]]) / len(negative_indices[group])
            plt.bar(n_groups + 1 + 2 * index, prob_1, color=color[index])
            plt.bar(n_groups + 2 + 2 * index, prob_0, color=color[index])
            x_tick_labels_by_label.extend(
                ["{} recidivism".format(group), "{} no recidivism".format(group)]
            )

    x_tick_labels = x_tick_labels_basic + x_tick_labels_by_label
    plt.xticks(
        range(1, len(x_tick_labels) + 1),
        x_tick_labels,
        rotation=45,
        horizontalalignment="right",
    )


class LogisticRegressionAsRegression(BaseEstimator, ClassifierMixin):
    def __init__(self, logistic_regression_estimator):
        self.logistic_regression_estimator = logistic_regression_estimator

    def fit(self, X, y):
        try:
            check_is_fitted(self.logistic_regression_estimator)
            self.logistic_regression_estimator_ = self.logistic_regression_estimator
        except NotFittedError:
            self.logistic_regression_estimator_ = clone(
                self.logistic_regression_estimator
            ).fit(X, y)
        return self

    def predict(self, X):
        # use predict_proba to get real values instead of 0/1, select only prob for 1
        scores = self.logistic_regression_estimator_.predict_proba(X)[:, 1]
        return scores


def process_for_threshold_optimizer(
    x_train, sensitive_attribute, sensitive_attribute_value
):
    binary_col_encoded = (
        x_train.loc[:, sensitive_attribute] == sensitive_attribute_value
    )
    x_train.loc[:, sensitive_attribute_value] = binary_col_encoded
    x_train = x_train.drop(columns=[sensitive_attribute])
    return x_train
