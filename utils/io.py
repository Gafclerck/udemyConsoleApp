class Io:
    @staticmethod
    def get_string(message:str):
        while True:
            string = input(message)
            if (string.strip()):
                break
        return string.strip()

    @staticmethod
    def get_int(message:str):
        while True:
            try:
                integer = int(input(message))
                return integer
            except ValueError:
                print("invalid input")
                
    @staticmethod
    def yes_or_no(question):
        """return True if yes else False"""
        while True:
            res = input(f"{question} {"[yes/no]"} : ")
            if res.lower() in ["", "y", "yes"]:
                return "yes"
            elif res.lower() in ["no", "n"]:
                return "no"
        