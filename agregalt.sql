SELECT 
    r.ration_id AS ration_id,
    r.start_date_time,
    r.end_date_time,

    COUNT(c.temp_1) AS meresek_szama,
    
  
    MIN(CAST(c.temp_1 AS REAL)) AS temp1_min,
    MAX(CAST(c.temp_1 AS REAL)) AS temp1_max,
    ROUND(AVG(CAST(c.temp_1 AS REAL)), 2) AS temp1_atlag,
    
    -- Panel 2
    MIN(CAST(c.temp_2 AS REAL)) AS temp2_min,
    MAX(CAST(c.temp_2 AS REAL)) AS temp2_max,
    ROUND(AVG(CAST(c.temp_2 AS REAL)), 2) AS temp2_atlag,
    
    -- Panel 3 
    MIN(CAST(c.temp_3 AS REAL)) AS temp3_min,
    MAX(CAST(c.temp_3 AS REAL)) AS temp3_max,
    ROUND(AVG(CAST(c.temp_3 AS REAL)), 2) AS temp3_atlag,
    
    -- Panel 4
    MIN(CAST(c.temp_4 AS REAL)) AS temp4_min,
    MAX(CAST(c.temp_4 AS REAL)) AS temp4_max,
    ROUND(AVG(CAST(c.temp_4 AS REAL)), 2) AS temp4_atlag,

    -- Panel 5
    MIN(CAST(c.temp_5 AS REAL)) AS temp5_min,
    MAX(CAST(c.temp_5 AS REAL)) AS temp5_max,
    ROUND(AVG(CAST(c.temp_5 AS REAL)), 2) AS temp5_atlag,
    
    -- Panel 6
    MIN(CAST(c.temp_6 AS REAL)) AS temp6_min,
    MAX(CAST(c.temp_6 AS REAL)) AS temp6_max,
    ROUND(AVG(CAST(c.temp_6 AS REAL)), 2) AS temp6_atlag,

    -- Panel 8 (temp_7 hiányzik)
    MIN(CAST(c.temp_8 AS REAL)) AS temp8_min,
    MAX(CAST(c.temp_8 AS REAL)) AS temp8_max,
    ROUND(AVG(CAST(c.temp_8 AS REAL)), 2) AS temp8_atlag,
    
    -- Panel 9
    MIN(CAST(c.temp_9 AS REAL)) AS temp9_min,
    MAX(CAST(c.temp_9 AS REAL)) AS temp9_max,
    ROUND(AVG(CAST(c.temp_9 AS REAL)), 2) AS temp9_atlag,


    -- Panel 10 
    MIN(CAST(c.temp_10 AS REAL)) AS temp10_min,
    MAX(CAST(c.temp_10 AS REAL)) AS temp10_max,
    ROUND(AVG(CAST(c.temp_10 AS REAL)), 2) AS temp10_atlag,
    
    -- Panel 11
    MIN(CAST(c.temp_11 AS REAL)) AS temp11_min,
    MAX(CAST(c.temp_11 AS REAL)) AS temp11_max,
    ROUND(AVG(CAST(c.temp_11 AS REAL)), 2) AS temp11_atlag,

    -- Panel 12
    MIN(CAST(c.temp_12 AS REAL)) AS temp12_min,
    MAX(CAST(c.temp_12 AS REAL)) AS temp12_max,
    ROUND(AVG(CAST(c.temp_12 AS REAL)), 2) AS temp12_atlag,
    
    -- Panel 13
    MIN(CAST(c.temp_13 AS REAL)) AS temp13_min,
    MAX(CAST(c.temp_13 AS REAL)) AS temp13_max,
    ROUND(AVG(CAST(c.temp_13 AS REAL)), 2) AS temp13_atlag,

    -- Panel 14
    MIN(CAST(c.temp_14 AS REAL)) AS temp14_min,
    MAX(CAST(c.temp_14 AS REAL)) AS temp14_max,
    ROUND(AVG(CAST(c.temp_14 AS REAL)), 2) AS temp14_atlag,
    
    -- Panel 15
    MIN(CAST(c.temp_15 AS REAL)) AS temp15_min,
    MAX(CAST(c.temp_15 AS REAL)) AS temp15_max,
    ROUND(AVG(CAST(c.temp_15 AS REAL)), 2) AS temp15_atlag
                    
FROM rations r
INNER JOIN cool_system c ON c.date_time BETWEEN r.start_date_time AND r.end_date_time
GROUP BY r.ration_id, r.start_date_time, r.end_date_time
ORDER BY r.ration_id;

