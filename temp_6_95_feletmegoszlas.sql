SELECT 
    r.ration_id,
    COUNT(c.temp_6) AS meresek_szama,

    SUM(CASE 
            WHEN c.temp_6 IS NOT NULL AND c.temp_6 > 95 AND c.temp_6 < 120
            THEN 1 
            ELSE 0 
        END) AS meresek_95fok_120fok_között,

    ROUND(
        100.0 * SUM(CASE 
                        WHEN c.temp_6 IS NOT NULL AND c.temp_6 > 95 AND c.temp_6 < 120
                        THEN 1 
                        ELSE 0 
                    END) / 
        NULLIF(COUNT(c.temp_6), 0), 2
    ) AS arany_95fok_felett_szazalek

FROM rations r
INNER JOIN cool_system c 
    ON c.date_time BETWEEN r.start_date_time AND r.end_date_time
GROUP BY r.ration_id;
