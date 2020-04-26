
import pyfiglet


class Code(object):
    def __init__(self):
        self.str = ""


class Import(object):

    def __init__(self, code):

        self.code = code.str
        self.imports = """
try:
    from flask import Flask
    from flask_restful import Resource, Api, reqparse
    import sys
    import os
    import json
    from flask import request
except Exception as e:
    print("Some Modules are Missing  ")
    
    
app = Flask(__name__)
api = Api(app)


"""
        self.code += self.imports


class Choice(object):

    def __init__(self, code):
        self.code = code

    def choice_select(self):

        print("\t1.GET Request ")
        print("\t2.POST Request ")
        print("\t3. Exit ")
        choice = input("")
        return choice

    def logic(self, choice):

        if choice is "1" or "2" or "3":

            if choice == "1":
                self.choice_1()

            if choice == "3":
                self.choice_3()

        else:
            print("Invalid Choice ! ")
            return -1

    def choice_1(self):
        """
        GET request
        """
        queryParams = []
        queryParams_type = []
        queryParams_request = []

        N = input("How Many Query Parameters  [0-9] ? ")

        for i in range(int(N)):
            queryParams.append(input("First Query Parameters ? "))
            queryParams_type.append(input("Type [str, int]: "))
            queryParams_request.append(input("Required [True, False] :"))

        data = list(zip(queryParams, queryParams_type,queryParams_request))

        parserArg = []
        for param in data:
            str = """parser.add_argument('{}', type={},required={} , help='{} Query Paramters ')""".format(param[0],
            param[1], param[2], param[0])
            parserArg.append(str)

        parserArg.insert(0, "\nparser = reqparse.RequestParser()")

        Parser_Args = '\n'.join(parserArg)
        self.code += "\n"
        self.code += "\n"

        code_constructor = []

        for params in data:
            code_constructor.append("\tself.{} = parser.parse_args().get("'{}'", None)".format(params[0], params[0]))

        code_constructor.append("\n")
        code_constructor.insert(0 , "def __init__(self):")
        code_constructor.insert(0, "class APIController(object):")
        code_constructor.insert(1, "\n")
        code_constructor_str = '\n\t'.join(code_constructor)

        lib_class = self.code
        lib_class += code_constructor_str       # code merges the imports and class and const

        get_str = []
        get_str.append("\n\tdef get(self):")
        get_str.append("\t\tpass")
        get_str.append("\n")

        lib_class_get = ""
        lib_class_get += lib_class + '\n'.join(get_str)

        final_get_code = ""
        final_get_code += lib_class_get + Parser_Args
        final_get_code += "api.add_resource(APIController, '/')"
        final_get_code += """


if __name__ == '__main__':
    app.run(debug=True)
        """
        print("Saving code on computer ....... ")

        with open("app.txt", "w") as f:
            f.writelines(final_get_code)

    def choice_3(self):
        """
        EXIT
        """

    def main(self):
        choice = self.choice_select()
        self.logic(choice)


def main():

    ascii_banner = pyfiglet.figlet_format("Flask API Generator ")
    print(ascii_banner)
    print("Author: Soumil Shah : shahsoumil519@gmail.com\n\n")



    code = Code()
    imp = Import(code)

    # Ask the User if they want to do Get POST
    choice = Choice(imp.code)
    choice.main()


if __name__ == "__main__":
    main()







