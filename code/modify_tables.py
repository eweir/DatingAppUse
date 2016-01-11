import psycopg2

conn = psycopg2.connect(dbname='capstone', user='ellenweir', host='/tmp')
c = conn.cursor()

c.execute(

    ''' CREATE TABLE grouped_by_user as
    SELECT u.user_id,
        u.num_connections,
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
        u.q_ans,
        u.connected,
        u.only_signup,
        u.engagement_level,
        e.engagement_level as max_engagement

    FROM engagement_df e
    INNER JOIN users_df u
    ON e.user_id = u.user_id;

    '''


conn.commit()
conn.close()
