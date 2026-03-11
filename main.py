
class Salad(MenuItem):
    def __init__(self, name, description, category, is_available, ingredients, dressing, is_vegan):
        super().__init__(name, description, category, is_available)
        self.ingredients = ingredients
        self.dressing = dressing
        self.is_vegan = is_vegan

    def prepare(self):
        super().prepare()
        print(f'Salat tarkibi: {self.ingredients}\n{self.dressing} ziravori bilan aralashtirilmoqda.')

    def serve(self):
        super().serve()
        print(f'{self.name} salat stolga qo‘yildi')

    def info(self):
        super().info()
        print(f'Tarkibi: {self.ingredients}')
        print(f'Ziravor turi: {self.dressing}')
        print(f'Bu Veganmi: {self.is_vegan}')
