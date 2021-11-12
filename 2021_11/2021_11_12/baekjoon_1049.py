#baekjoon_1049_기타줄

#=== import module ===#

#=== Function define ===#

#=== variable declare ===#
need_string = 0; brand_string = 0; #필요한 기타줄 수, 기타줄 브랜드 수
price_info = [];
package_price = 0;
each_price = 0;
min_each_price = 1000;
min_package_price = 1000;
p = 0; q = 0; #몫과 나머지
min_pay_price = 0; #최소 지불 가격
#=== main function ===#
need_string, brand_string = map(int, input().split());

for _ in range(brand_string):
  package_price, each_price = map(int, input().split());
  price_info.append([package_price,each_price]);

#min_each_price , min_package_price 찾기
for info in price_info:
  if info[0] < min_package_price:
    min_package_price = info[0];
  if info[1] < min_each_price:
    min_each_price = info[1];

p = int(need_string / 6);
q = need_string % 6;

#낱개로 사는 게 패키지보다 더 쌀 경우
if min_each_price * 6 < min_package_price:
  min_pay_price = min_each_price * need_string;
else: #패캐지로 사는 게 더 쌀 경우
  min_pay_price += p * min_package_price + q * min_each_price;

if min_pay_price > (p+1) * min_package_price:
  min_pay_price = (p+1) * min_package_price;

print(min_pay_price);
