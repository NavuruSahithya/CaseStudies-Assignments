INSERT INTO Customers VALUES
(1, 'Rahul', 'Hyderabad'),
(2, 'Anita', 'Chennai'),
(3, 'Kiran', 'Bangalore'),
(4, 'Sneha', 'Mumbai');  -- inactive customer

INSERT INTO Products VALUES
(101, 'Laptop', 'Electronics', 50000),
(102, 'Phone', 'Electronics', 20000),
(103, 'Shoes', 'Fashion', 3000),
(104, 'Watch', 'Fashion', 5000);

INSERT INTO Orders VALUES
(1, 1, '2026-04-01'),
(2, 2, '2026-04-02'),
(3, 1, '2026-04-05');

INSERT INTO Order_Items VALUES
(1, 101, 1),
(1, 103, 2),
(2, 102, 1),
(3, 104, 1);