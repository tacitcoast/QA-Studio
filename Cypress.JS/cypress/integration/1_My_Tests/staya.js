
describe('Тестирование staya', function () {
    
    it('Проваливаюсь в категорию поводки и ищу совпадение с названием Heatwave', function () {
        cy.visit('https://staya.dog/');
        cy.contains('input', 'Поводки').click();
        cy.contains('Heatwave');
        cy.end();
         })

     it('search something', function () {
        cy.visit('https://staya.dog/');
        })
})
