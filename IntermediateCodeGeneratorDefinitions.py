from EnumIntermediateCodeDefinitions import IntermediateCodeType
from IntermediateCodeInterfaces import (
    IFunctionIntermediateGenerator,
    ITypeDefinitionIntermediateGenerator,
    IMainIntermediateGenerator,
)
from ExpressionDefinitions import Expression


class FunctionIntermediateCodeGenerator(IFunctionIntermediateGenerator):

    def __init__(self, name, params, locals_vars, body):
        """
        name: nombre de la funcion
        params,locals -> list(str): los nombres de las variables
        body -> IMainIntermediateGenerator
        """
        self._name = name
        self._params = params
        self._locals = locals_vars
        self._body = body
        pass

    @property
    def Type(self):
        return IntermediateCodeType.Function

    @property
    def Params(self):
        return self._params

    @property
    def ID(self):
        return self._name

    @property
    def Template(self):

        template = f"function {self._name} " + "{"

        for param in self._params:
            template += f"PARAM {param};\n"
            pass

        for local in self._locals:
            template += f"LOCAL {local};\n"
            pass

        template += self._body.Template + "\n}\n"
        return template

    pass


class TypeIntermediateCodeGenerator(ITypeDefinitionIntermediateGenerator):

    def __init__(self, name, attributes, functions, ascendence):
        """
        functions -> dict<str,str>
        diccionario con los nombres y los id de las funciones
        properties -> list(str)
        nombres propiedades internas de la definicion de tipo
        ascendence -> list(ITypeIntermediateGenerator)
        lista de los tipos de los que hereda
        """
        self._name = name
        self._attributes = attributes
        self._functions = functions
        self._ascendence = ascendence
        pass

    @property
    def Name(self):
        return self._name

    @property
    def Attributtes(self):
        return self._attributes

    @property
    def Functions(self):
        return self._functions

    @property
    def Ascendence(self):
        return self._ascendence

    @property
    def Type(self):
        return IntermediateCodeType.TypeDefinition

    @property
    def Template(self):

        template = f"type {self._name} " + "{"

        for father in self._ascendence:
            for attribute in father.Attributes:
                template += f"attribute {attribute};\n"
                pass
            pass
        for attribute in self._attributes:
            template += f"attribute {attribute};\n"
            pass

        for father in self._ascendence:
            for function in father.Functions.keys():
                template += f"method {function} : {father.Functions[function]};\n"
                pass
            pass

        for function in self._functions.keys():
            template += f"method {function} : {self._functions[function]}"
            pass

        template += "\n}\n"
        return template

    pass


class MainIntermediateCodeGenerator(IMainIntermediateGenerator):

    pass


class DataIntermediateCodeGenerator:
    def __init__(self, data) -> None:
        self._data = data
        pass

    @property
    def Template(self):
        template = f".DATA \n"
        for i in self._data:
            template += f"s{i} =" + '"' + "{self._data[i]}" + '" \n'
