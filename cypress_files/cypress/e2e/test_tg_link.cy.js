/// <reference types="cypress" />

it("should open site", () => {
    cy.visit("https://google.ru");
    cy.get('[name="q"]').type("Byndyusoft");
    cy.contains('Поиск в Google').click();
    cy.get('[jsname="UWckNb"]').first().invoke('removeAttr', 'target').click();

    cy.origin('https://byndyusoft.com/', () => {
        cy.get('.btn--info.js-popup-callback-show').click();
        cy.get('.popup-callback__contacts-tg').should('have.attr', 'href').and('include', 'https://t.me/alexanderbyndyu')
      })
});
