
class Evaluator:

    @staticmethod
    def zip_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1

        result = [x * len(y) for x, y in zip(coefs, words)]
        print(sum(result))

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        result = 0
        for i, val in enumerate(words):
            result += len(val) * coefs[i]
        print(result)
