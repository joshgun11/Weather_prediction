import argparse



class KParser():
    def __init__(self) -> None:
        self.parser = parser = argparse.ArgumentParser()
        self.parser = argparse.ArgumentParser()
        
        self.parser.add_argument("--test_size", help="test size", action='store', nargs='?', default=0.2,
                            type=float)
        self.parser.add_argument("--model_type", help="model type", action='store', nargs='?', default='linear_reg',
                            type=str)   
        self.parser.add_argument("--df", help="model type", action='store', nargs='?', default='weather',
                            type=str)
                               

    def parse_args(self):
        return self.parser.parse_args()

    def parse_args_list(self, args_list):
        return self.parser.parse_args(args_list)