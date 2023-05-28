class Component:
    def __init__(self, name, structure):
        self.name = name
        self.structure = structure

    def print(self):
        print(self.structure)


class ComponInput(Component):
    def __init__(self):
        name = "input"
        structure = f'<input name="{name}">'
        super().__init__(name, structure)


class ComponSelect(Component):
    def __init__(self):
        name = "select"
        structure = f'<select name="{name}"></select>'
        super().__init__(name, structure)


class ComponRadioButton(Component):
    def __init__(self):
        name = "radio button"
        structure = f'<radio name="{name}">'
        super().__init__(name, structure)


class Fieldset(Component):
    def __init__(self):
        name = "fieldset"
        structure = ""
        super().__init__(name, structure)
        self.elements = []

    def addElem(self, elem):
        self.elements.append(elem)

    def print(self):
        print(f'<{self.name}>')

        for elem in self.elements:
            elem.print()

        print(f'</{self.name}>')


class Form(Component):
    def __init__(self):
        name = "form"
        structure = ""
        super().__init__(name, structure)
        self.elements = []

    def addElem(self, elem):
        self.elements.append(elem)

    def print(self):
        print(f'<{self.name}>')

        for elem in self.elements:
            elem.print()

        print(f'</{self.name}>')


fieldset_1 = Fieldset()
fieldset_1.addElem(ComponInput())
fieldset_1.addElem(ComponRadioButton())

fieldset_2 = Fieldset()
fieldset_2.addElem(ComponInput())
fieldset_2.addElem(ComponSelect())
fieldset_2.addElem(fieldset_1)

form_1 = Form()
form_1.addElem(ComponInput())
form_1.addElem(ComponSelect())
form_1.addElem(fieldset_2)

form_1.print()
