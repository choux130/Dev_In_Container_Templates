DROP PROCEDURE IF EXISTS GetTopNCityByCountry_Count;

DELIMITER //
CREATE PROCEDURE GetTopNCityByCountry_Count(IN top_n int, IN min_n int, OUT total_num_rows int)
BEGIN
    WITH cit_add_wf AS
    (
        select
            *, 
            ROW_NUMBER() OVER (PARTITION BY CountryCode ORDER BY Population ASC) as rank_in_country,
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
    SELECT 
    	count(*) INTO total_num_rows
    from city_filter; 

END //
DELIMITER ;

# call the procedure
CALL GetTopNCityByCountry_Count(3, 20, @total_num_rows);
SELECT @total_num_rows AS total_num_rows;
