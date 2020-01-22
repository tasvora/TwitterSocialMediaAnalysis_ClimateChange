CREATE TABLE TweetPreview(
	id VARCHAR  NOT NULL,
	author_id VARCHAR NOT NULL,
	text VARCHAR NOT NULL,
	retweets INT,
	permalink VARCHAR,
	date DATE NOT NULL,
	formatted_date DATE NOT NULL,
	favorites VARCHAR,
	mentions VARCHAR,
	hashtags VARCHAR,
	search_hashtags VARCHAR,
	location VARCHAR
);
											

ALTER TABLE TweetPreview
	add column tweetid
	serial Primary Key;	
	