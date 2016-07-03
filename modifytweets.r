# Map 1-based optional input ports to variables
dataset <- maml.mapInputPort(1) # class: data.frame

# Separate the label and tweet text
#sentiment_label <- dataset[[1]]
sentiment_label <- rep(0, length(dataset[[1]]))
tweet_text      <- dataset[[1]]

#Remove links
tweet_text <- gsub('(?P<url>https?://[^\\s]+)', '', tweet_text, ignore.case = TRUE, perl=TRUE)

#Replace Names
tweet_text <- gsub('@(\\w+)', 'name', tweet_text, ignore.case = TRUE)

# Replace punctuation, special characters and digits with space
tweet_text <- gsub("[^a-z]", " ", tweet_text, ignore.case = TRUE)

# Convert to lowercase
tweet_text <- sapply(tweet_text, tolower)

data.set <- as.data.frame(cbind(sentiment_label,tweet_text), 
	stringsAsFactors=FALSE)                 

# Select data.frame to be sent to the output Dataset port
maml.mapOutputPort("data.set")