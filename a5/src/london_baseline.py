# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
import utils
import argparse

argp = argparse.ArgumentParser()
argp.add_argument('--eval_corpus_path',
    help="Path of the corpus to evaluate on", default=None)
args = argp.parse_args()

with open(args.eval_corpus_path) as fin:
    lines = [x.strip().split('\t') for x in fin]
nlines = len(lines)
total, correct = utils.evaluate_places(args.eval_corpus_path, ["London"]*nlines)

print("Baseline: Predicting 'London' for every example")
print("Total examples: {}".format(total))
print("Correct predictions: {}".format(correct))
print("Accuracy: {:.2f}%".format(100*correct/total))