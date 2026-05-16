# Step 1: Store the available cash in a variable called kitty
kitty = 500

# Step 2: Create an empty list called requests
requests = []

# Step 3: Read the data from the text file line by line
with open('loan_requests.txt', 'r') as f:
  for line in f:
    requests.append(int(line.strip()))
    
# Step 4: Loop through all requests and process each one
for request in requests:
  
  # Case 1: Kitty is empmty - cannot pay anything
  if kitty == 0:
    print("Request for ", request, "went unpaid - kitty is empty")
    with open('loan_requests.txt', 'a') as f:
      f.write("\nRequest for " + str(request) + " went unpaid - kitty is empty")
      
  # Case 2: Partial payment - request exceed what's left in kitty
  elif request > kitty:
    print("Request for ", request, " partial payment of ", kitty, " was made")
    with open('loan_requests.txt', 'a') as f:
      f.write("\nRequest for " + str(request) + " partial payment of " + str(kitty) + " was made")
    kitty = 0 # Kitty is now empty after the partial payment
    
  # Case 3: Full payment - enough money in Kitty
  else:
    print("Request for ", request, " was paid in full")
    with open('loan_requests.txt', 'a') as f:
      f.write("\nRequest for " + str(request) + " was paid in full")
    kitty -= request # deduct the loan from the kitty