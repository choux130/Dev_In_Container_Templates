DROP PROCEDURE IF EXISTS GetTopNCityByCountry;

DELIMITER //
CREATE PROCEDURE GetTopNCityByCountry(IN top_n int, IN min_n int)
BEGIN
    WITH cit_add_wf AS
    (
        select
            *, 
            ROW_NUMBER() OVER (PARTITION BY CountryCode ORDER BY Population ASC, Name ASC) as rank_in_country,
            COUNT(*) OVER (PARTITION BY CountryCode) as count_in_country
        FROM 
            city
    ),
    city_filter as (
        select * 
        from cit_add_wf
        WHERE 
            rank_in_country >= 1 AND 
            rank_in_country <= top_n AND 
            count_in_country >= min_n
    )
    SELECT * 
    from city_filter 
    ORDER BY countrycode ASC, rank_in_country ASC, count_in_country ASC;

END //
DELIMITER ;

# call the procedure
CALL GetTopNCityByCountry(3, 20);
