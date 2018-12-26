DELIMITER $$
USE `test`

$$
CREATE PROCEDURE `spCreateUser` (
IN p_name varchar(50),
IN p_password varchar(50)
)
BEGIN

if ( select exists (select 1 from users where name = p_name) ) THEN

    select 'Username Exists !!';

ELSE

insert into users
(
    name,
    password
)
values
(
    p_name,
    p_password
);

END IF;

END
$$

DELIMITER ;

----------------------------------------------------------------------

DELIMITER $$
USE `test`

$$
CREATE PROCEDURE `spGetListUser` (
IN p_name varchar(50),
IN p_password varchar(50)
)
BEGIN

if ( select exists (select 1 from users where name = p_name) ) THEN

    select 'Username Exists !!';

ELSE

insert into users
(
    name,
    password
)
values
(
    p_name,
    p_password
);

END IF;

END
$$

DELIMITER ;
