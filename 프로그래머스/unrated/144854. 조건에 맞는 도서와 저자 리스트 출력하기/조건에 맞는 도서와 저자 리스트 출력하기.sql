-- 코드를 입력하세요
SELECT BOOK_ID, AUTHOR_NAME, DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d')
FROM book
LEFT JOIN author ON book.author_id = author.author_id
WHERE category = '경제'
ORDER BY PUBLISHED_DATE ASC