-- 코드를 입력하세요
select CAR_TYPE, count(*) as CARS
from car_rental_company_car
where (options LIKE '%통풍시트%') or (options LIKE '%열선시트%') or (options LIKE '%가죽시트%')
group by car_type
order by car_type asc
