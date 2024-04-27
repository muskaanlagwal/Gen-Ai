def chatbot(query):
    if query == "What was Microsoft's total revenue in 2023?":
        return "Microsoft's total revenue in 2023 was $211,915 million."
    elif query == "How did Tesla's net income change from 2021 to 2022?":
        return "Tesla's net income increased from $5,644 million in 2021 to $12,587 million in 2022, marking a significant growth of $6,943 million."
    elif query == "What was Apple's total assets in 2022?":
        return "Apple's total assets in 2022 amounted to $352,755 million."
    elif query == "What was the total cash flow from operations for Microsoft in 2022?":
        return "Microsoft's total cash flow from operations in 2022 was $89,035 million."
    elif query == "How did Apple's total liabilities change from 2021 to 2023?":
        return "Apple's total liabilities increased from $0 million in 2021 to $290,437 million in 2023, indicating significant financial obligations acquired during this period."
    elif query == "What was the net income for Tesla in 2023?":
        return "Tesla's net income in 2023 amounted to $14,974 million."
    elif query == "How did Microsoft's total assets change from 2021 to 2022?":
        return "Microsoft's total assets increased from $0 million in 2021 to $364,840 million in 2022, reflecting substantial growth in its asset base."
    elif query == "What was the total revenue for Apple in 2021?":
        return "Apple's total revenue in 2021 was $365,817 million."
    elif query == "How did Tesla's cash flow from operations change from 2022 to 2023?":
        return "Tesla's cash flow from operations decreased from $14,724 million in 2022 to $13,256 million in 2023, indicating a slight decline in operational cash generation."
    elif query == "What was the net income margin for Microsoft in 2022?":
        return "Microsoft's net income margin in 2022 was approximately 36.7%, calculated by dividing the net income ($72,738 million) by the total revenue ($198,270 million) and multiplying by 100."
    elif query == "How did Apple's total assets change from 2022 to 2023?":
        return "Apple's total assets increased from $352,755 million in 2022 to $352,583 million in 2023, indicating a slight decrease."
    elif query == "What was the total liabilities for Tesla in 2022?":
        return "Tesla's total liabilities in 2022 amounted to $36,440 million."
    elif query == "How did Microsoft's cash flow from operations change from 2022 to 2023?":
        return "Microsoft's cash flow from operations decreased from $89,035 million in 2022 to $87,582 million in 2023, indicating a slight decline in operational cash generation."
    elif query == "What was the net income margin for Tesla in 2021?":
        return "Tesla's net income margin in 2021 was approximately 10.5%, calculated by dividing the net income ($5,644 million) by the total revenue ($53,823 million) and multiplying by 100."
    elif query == "How did Apple's cash flow from operations change from 2021 to 2023?":
        return "Apple's cash flow from operations increased from $104,038 million in 2021 to $110,543 million in 2023, indicating a positive trend in operational cash generation."
    else:
        return "Sorry, I couldn't find the information for that query."

# Test the chatbot
user_query = input("Ask a financial question: ")
response = chatbot(user_query)
print(response)
