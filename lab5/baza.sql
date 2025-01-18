
CREATE DATABASE IF NOT EXISTS warehouse;


USE warehouse;


CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL, -- Nazwa produktu
    quantity INT NOT NULL,      -- Ilość na stanie
    price DECIMAL(10, 2) NOT NULL -- Cena jednostkowa
);


CREATE TABLE IF NOT EXISTS transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,                 -- ID produktu
    quantity_change INT NOT NULL,            -- Zmiana ilości (pozytywna/negatywna)
    transaction_type VARCHAR(50) NOT NULL,   -- Typ operacji (np. Dodanie, Sprzedaż)
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Czas operacji
    FOREIGN KEY (product_id) REFERENCES products(id) -- Klucz obcy do tabeli `products`
);
