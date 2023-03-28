CREATE TABLE top_income AS
SELECT manufacturer, model, CAST(AVG(household_income) AS INT) as avg_income
FROM FCV
WHERE household_income > 250000
GROUP BY manufacturer, model
ORDER BY avg_income DESC;

select * from top_income

drop table top_income