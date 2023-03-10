SET @now = NOW(), @current_date = CURDATE(), @current_time = CURRENT_TIME();
SELECT 
	@now AS now, 
	@current_date AS curdate, 
    @current_time AS curtime;
