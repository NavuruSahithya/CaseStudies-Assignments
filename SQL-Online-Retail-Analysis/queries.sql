
#Top-Selling Products
SELECT p.name, SUM(oi.quantity) AS total_sold
FROM Order_Items oi
JOIN Products p ON oi.product_id = p.product_id
GROUP BY p.name
ORDER BY total_sold DESC;


#Most Valuable Customers
SELECT c.name, SUM(p.price * oi.quantity) AS total_spent
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
JOIN Order_Items oi ON o.order_id = oi.order_id
JOIN Products p ON oi.product_id = p.product_id
GROUP BY c.name
ORDER BY total_spent DESC;


#Monthly Revenue Calculation
SELECT SUBSTR(o.order_date, 1, 7) AS month,
       SUM(p.price * oi.quantity) AS revenue
FROM Orders o
JOIN Order_Items oi ON o.order_id = oi.order_id
JOIN Products p ON oi.product_id = p.product_id
GROUP BY month;

#Category-wise Sales Analysis
SELECT p.category, SUM(p.price * oi.quantity) AS total_sales
FROM Products p
JOIN Order_Items oi ON p.product_id = oi.product_id
GROUP BY p.category;


#Detect Inactive Customers
SELECT name
FROM Customers
WHERE customer_id NOT IN (
    SELECT DISTINCT customer_id FROM Orders
);