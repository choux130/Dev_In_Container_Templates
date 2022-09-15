library(dplyr)
library(plumber)

pr("./src/plumber.R") %>%
  pr_run(host='0.0.0.0', port=5050)
