class ICodeIntermediateGenerator:

    @property
    def Type(self):
        """
        Type() -> IntermediateCodeType
        devuelve el tipo de generador de codigo que representa
        """

        raise NotImplementedError()

    @property
    def Template(self):
        """
        Template() -> str
        devuelve la plantilla de codigo intermedio correspondiente
        """

        raise NotImplementedError()

    pass


class IFunctionIntermediateGenerator(ICodeIntermediateGenerator):

    @property
    def Params(self):
        """
        Params() -> str
        devuelve un diccionario con los nombres y los tipos de los parametros de la funcion
        """

        raise NotImplementedError()

    @property
    def ID(self):
        """
        devuelve el identificador de la funcion
        """

        raise NotImplementedError()

    pass


class ITypeDefinitionIntermediateGenerator(ICodeIntermediateGenerator):

    @property
    def Name(self):
        """
        nombre del tipo que define
        """

        raise NotImplementedError()

    @property
    def Attributtes(self):
        """
        Attributtes() -> list(str)
        devuelve una lista con los nombres de los atributos internos del tipo
        """

        raise NotImplementedError()

    @property
    def Functions(self):
        """
        Functions() -> dict<str,str>
        devuelve undiccionario con los nombres de las funciones y los id de cada metodo
        """

        raise NotImplementedError()

    @property
    def Ascendence(self):
        """
        Ascendence() -> list(ITypeIntermediateGenerator)
        devuelve una lista con los nombres de los tipos de los que hereda
        """

        raise NotImplementedError()

    pass


class IDataIntermediateCodeGenerator(ICodeIntermediateGenerator):
    @property
    def Data(self):
        """
        Data() -> <str,str>
        devuelve un diccionario con las variables y los valores
        """


class IMainIntermediateGenerator(ICodeIntermediateGenerator):

    @property
    def Variables(self):
        """
        Variables() -> dict<str,str>
        devuelve un diccionario con los nombres de las variables y sus tipos
        """

        raise NotImplementedError()

    pass
