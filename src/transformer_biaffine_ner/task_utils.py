# coding=utf-8
# Created by bugface (https://github.com/bugface)
# First created at 12/31/21

from transformer_ner.model_utils import PGD, FGM
from transformer_ner.task import save_model, load_model
from transformer_ner.model_utils import get_linear_schedule_with_warmup


def _get_predict_labels(args, model, features):
    y_trues, y_preds = [], []
    eval_loss = .0
    model.eval()

    return y_trues, y_preds, round(eval_loss, 4)


def _evaluate():
    pass


def predict(args, model, features):
    # for biaffine, we set 'O' index to 0 by default, other annotated types will be 1, 2, ...
    system_labels = {label for idx, label in args.idx2label.items()}


def train():
    pass


