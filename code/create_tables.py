import psycopg2

conn = psycopg2.connect(dbname='capstone', user='ellenweir', host='/tmp')
c = conn.cursor()


#Create table with question body and answer body, joined on question id

c.execute(

    '''
    CREATE TABLE question_answers as
    SELECT a.user_id,
        q.id as question_id,
        q.sponsor_id,
        q.body as question_body,
        a.body as ans_body,
        q.answers_count
    FROM questions q LEFT JOIN answers a
    ON a.question_id=q.id;
    '''
)

#Create table with count of number of connections for each user

c.execute(

    ''' CREATE TABLE connection_count as
    SELECT user_id, count (*)
    FROM connections
    GROUP BY user_id;
    '''
)

#Create table with user information and question/answer content

c.execute(

    ''' CREATE TABLE user_qs as
    SELECT u.id as user_id,
        qa.question_id,
        qa.sponsor_id,
        qa.question_body,
        qa.ans_body,
        qa.answers_count,
        u.gender,
        u.display_name,
        u.location,
        u.birthdate,
        u.occupation,
        u.created_at,
        u.updated_at,
        u.education,
        u.height,
        u.city,
        u.min_age,
        u.max_age,
        u.search_proximity,
        u.region,
        u.visible_to,
        u.last_seen_at,
        u.latitude,
        u.longitude

    FROM users u
    LEFT JOIN question_answers qa
    ON qa.user_id=u.id;

    '''
)

#Create table with all user data and number of connections for each user

c.execute(

    ''' CREATE TABLE user_qs_conn as
    SELECT u.user_id,
        c.count as num_connections,
        u.question_id,
        u.sponsor_id,
        u.question_body,
        u.ans_body,
        u.answers_count,
        u.gender,
        u.display_name,
        u.location,
        u.birthdate,
        u.occupation,
        u.created_at,
        u.updated_at,
        u.education,
        u.height,
        u.city,
        u.min_age,
        u.max_age,
        u.search_proximity,
        u.region,
        u.visible_to,
        u.last_seen_at,
        u.latitude,
        u.longitude

    FROM user_qs u
    LEFT JOIN connection_count c
    ON c.user_id=u.user_id;

    '''
)

c.execute(

    ''' CREATE TABLE users_trimmed as
    SELECT id,
        gender,
        location,
        birthdate,
        occupation,
        created_at,
        updated_at,
        education,
        height,
        city,
        min_age,
        max_age,
        search_proximity,
        region,
        visible_to,
        last_seen_at,
        latitude,
        longitude

    FROM users;

    '''
)

c.execute(

    ''' CREATE TABLE all_info as
    SELECT u.id as user_id,
        q.id as question_id,
        q.sponsor_id,
        q.body as question_body,
        q.created_at as question_created,
        a.body as ans_body,
        q.answers_count,
        a.created_at as ans_created,
        c.count as num_connections,
        u.gender,
        u.display_name,
        u.location,
        u.birthdate,
        u.occupation,
        u.created_at,
        u.updated_at,
        u.education,
        u.height,
        u.city,
        u.min_age,
        u.max_age,
        u.search_proximity,
        u.region,
        u.visible_to,
        u.last_seen_at,
        u.latitude,
        u.longitude

    FROM users u
    LEFT JOIN connection_count c
    ON c.user_id=u.id
    LEFT JOIN answers a
    ON u.id=a.user_id
    LEFT JOIN questions q
    ON a.question_id=q.id;
    '''
)

c.execute(
    '''CREATE TABLE block_info as
    SELECT a.user_id,
        a.question_id,
        a.sponsor_id,
        a.question_body,
        a.question_created,
        a.ans_body,
        a.answers_count,
        a.ans_created,
        a.num_connections,
        a.gender,
        a.display_name,
        a.location,
        a.birthdate,
        a.occupation,
        a.created_at,
        a.updated_at,
        a.education,
        a.height,
        a.city,
        a.min_age,
        a.max_age,
        a.search_proximity,
        a.region,
        a.visible_to,
        a.last_seen_at,
        a.latitude,
        a.longitude,
        b.origin as block_origin,
        b.created_at as block_created,
        b.id as block_id
    FROM all_info a
    LEFT JOIN blocks b
    ON a.user_id=b.user_id
    WHERE origin='t';
    '''
)

c.execute(
    '''CREATE TABLE message_info as
    SELECT a.user_id,
        a.question_id,
        a.sponsor_id,
        a.question_body,
        a.question_created,
        a.ans_body,
        a.answers_count,
        a.ans_created,
        a.num_connections,
        a.gender,
        a.display_name,
        a.location,
        a.birthdate,
        a.occupation,
        a.created_at,
        a.updated_at,
        a.education,
        a.height,
        a.city,
        a.min_age,
        a.max_age,
        a.search_proximity,
        a.region,
        a.visible_to,
        a.last_seen_at,
        a.latitude,
        a.longitude,
        m.created_at as message_created,
        m.conversation_id as message_id
    FROM all_info a
    Right JOIN notifications m
    ON a.user_id=m.sender_id;
    '''
)

c.execute(
    '''CREATE TABLE messages as
    SELECT n. *
    FROM notifications n
    WHERE n.created_at = (SELECT MAX(n2.created_at)
                          FROM notifications n2
                          WHERE n2.sender_id = n.sender_id);
    '''
)

c.execute(
    '''CREATE TABLE messages2 as
    SELECT n. *
    FROM notifications n
    LEFT OUTER JOIN notifications n2
    ON n.sender_id = n2.sender_id
    AND (n.created_at < n2.created_at)
    OR (n.created_at = n2.created_at AND n.sender_id < n2.sender_id)
    WHERE n2.sender_id IS NULL;
    '''
)
#c.created_at as connection_created,

conn.commit()
conn.close()
