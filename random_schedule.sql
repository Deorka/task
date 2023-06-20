SET @counter = 0; SET @date = NOW(); set @rand1 = 0;
    WHILE @counter < 100 DO
        SET @counter = @counter + 1;
        SET @date = TIMESTAMPADD(DAY, @rand1, @date);
        SET @rand1 = FLOOR(RAND() * 6) + 2;
        SELECT DATE_FORMAT(@date, "%d.%m.%Y");
    END WHILE;
