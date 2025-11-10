SELECT 
    r.ration_id AS ration_id,
    r.start_date_time,
    r.end_date_time,
    COUNT(c.temp_1) AS meresek_szama,
	
	-- Panel 1 
    MIN(c.temp_1) AS temp1_min,
    MAX(c.temp_1) AS temp1_max,
    ROUND(AVG(c.temp_1), 2) AS temp1_atlag,
    
    -- Panel 2
    MIN(c.temp_2) AS temp2_min,
    MAX(c.temp_2) AS temp2_max,
    ROUND(AVG(c.temp_2), 2) AS temp2_atlag,
    
    -- Panel 3 
    MIN(c.temp_3) AS temp3_min,
    MAX(c.temp_3) AS temp3_max,
    ROUND(AVG(c.temp_3), 2) AS temp3_atlag,
    
    -- Panel 4
    MIN(c.temp_4) AS temp4_min,
    MAX(c.temp_4) AS temp4_max,
    ROUND(AVG(c.temp_4), 2) AS temp4_atlag,

	-- Panel 5
    MIN(c.temp_5) AS temp5_min,
    MAX(c.temp_5) AS temp5_max,
    ROUND(AVG(c.temp_5), 2) AS temp5_atlag,
    
    -- Panel 6
    MIN(c.temp_6) AS temp6_min,
    MAX(c.temp_6) AS temp6_max,
    ROUND(AVG(c.temp_6), 2) AS temp6_atlag,

	-- Panel 8 
    MIN(c.temp_8) AS temp8_min,
    MAX(c.temp_8) AS temp8_max,
    ROUND(AVG(c.temp_8), 2) AS temp8_atlag,
    
    -- Panel 9
    MIN(c.temp_9) AS temp9_min,
    MAX(c.temp_9) AS temp9_max,
    ROUND(AVG(c.temp_9), 2) AS temp9_atlag,


	-- Panel 10 
    MIN(c.temp_10) AS temp10_min,
    MAX(c.temp_10) AS temp10_max,
    ROUND(AVG(c.temp_10), 2) AS temp10_atlag,
    
    -- Panel 11
    MIN(c.temp_11) AS temp11_min,
    MAX(c.temp_11) AS temp11_max,
    ROUND(AVG(c.temp_11), 2) AS temp11_atlag,

	-- Panel 12
    MIN(c.temp_12) AS temp12_min,
    MAX(c.temp_12) AS temp12_max,
    ROUND(AVG(c.temp_12), 2) AS temp12_atlag,
    
    -- Panel 13
    MIN(c.temp_13) AS temp13_min,
    MAX(c.temp_13) AS temp13_max,
    ROUND(AVG(c.temp_13), 2) AS temp13_atlag,

	-- Panel 14
    MIN(c.temp_14) AS temp14_min,
    MAX(c.temp_14) AS temp14_max,
    ROUND(AVG(c.temp_14), 2) AS temp14_atlag,
    
    -- Panel 15
    MIN(c.temp_15) AS temp15_min,
    MAX(c.temp_15) AS temp15_max,
    ROUND(AVG(c.temp_15), 2) AS temp15_atlag
					
FROM rations r
INNER JOIN cool_system c ON c.date_time BETWEEN r.start_date_time AND r.end_date_time
GROUP BY r.ration_id, r.start_date_time, r.end_date_time
ORDER BY r.ration_id;


