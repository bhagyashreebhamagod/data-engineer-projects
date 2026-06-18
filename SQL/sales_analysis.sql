-- Sales Data Analysis

-- Total sales by region
SELECT region, SUM(sales) AS total_sales
FROM sales
GROUP BY region;

-- Top 5 products
SELECT product, SUM(sales) AS total_sales
FROM sales
GROUP BY product
ORDER BY total_sales DESC
LIMIT 5;

-- Monthly sales trend
SELECT month, SUM(sales) AS total_sales
FROM sales
GROUP BY month
ORDER BY month;
