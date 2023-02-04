
describe('Тестирование главной гугла', function () {
   it('Проверка, что при поиске теслы в выдаче есть тесла', function () {
        cy.visit('https://google.com');
        cy.get("input[type='text']").type('tesla').type('{enter}');
        cy.contains('https://www.tesla.com');
    })
})
