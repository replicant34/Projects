# Load necessary libraries
install.packages("tidyverse")
library(tidyverse)

# Load the Iris dataset
data(iris)

# View the first few rows of the dataset
head(iris)

# Summary statistics of the dataset
summary(iris)

# Check for missing values
sum(is.na(iris))

# Plot pairwise relationships
pairs(iris[, 1:4], main = "Pairwise Relationships in Iris Data", pch = 21, bg = c("red", "green3", "blue")[unclass(iris$Species)])

# Boxplot for each feature by species
iris_long <- gather(iris, key = "Feature", value = "Value", -Species)
ggplot(iris_long, aes(x = Species, y = Value, fill = Species)) +
  geom_boxplot() +
  facet_wrap(~Feature, scales = "free") +
  labs(title = "Boxplot of Iris Features by Species") +
  theme_minimal()

# Scatter plot of Sepal.Length vs Sepal.Width colored by Species
ggplot(iris, aes(x = Sepal.Length, y = Sepal.Width, color = Species)) +
  geom_point(size = 3) +
  labs(title = "Sepal Length vs Sepal Width", x = "Sepal Length", y = "Sepal Width") +
  theme_minimal()

# Save the plots
ggsave("pairwise_relationships.png")
ggsave("boxplot_iris_features.png")
ggsave("scatter_sepal_length_width.png")


