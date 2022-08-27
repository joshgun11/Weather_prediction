from parsers import KParser
from models import Models
from preapre_data import Prepare
import sys

class train():
    def __init__(self) -> None:
        pass

    def train_model(self,args):

        pre_process = Prepare()
        models = Models()
        df = args.df
        data = pre_process.load_data(df)
        X_train,X_test,y_train,y_test = pre_process.split_data(data,args.test_size)
        X_train_transformed,X_test_transformed = pre_process.normalize_features(X_train,X_test)
        print(X_train_transformed.shape)
        if args.model_type == 'linear_reg':
            models.linear_regression(X_train_transformed,X_test_transformed,y_train,y_test)


if __name__ == '__main__':
 
    parser = KParser()
    args = parser.parse_args()

    flag = len(sys.argv) == 1



    print("model_type:", args.model_type)
    print("test_size:", args.test_size)
    print("data:", args.df)



    train().train_model(args)






