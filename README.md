# WAF-AI

## Objective☄️
The growing complexity of cybersecurity threats demands innovative solutions that are adaptive to protect critical web infrastructure, scalable and cost-effective. This thesis introduces an AI Web Application Firewall (AI-WAF) capable of recording, analysing and mitigating web traffic threats. The AI-WAF automates threat detection, leverages supervised and unsupervised learning models and continuously adapts to emerging attack vectors. Key features include real-time traffic recording, anomaly detection, threat classification, automated mitigation, and an explainability layer for trust and transparency. Deployable as a reverse proxy with scalability and high availability. Continuous learning capabilities ensure the system adapts to emerging threats, while explainable AI tools like LIME and SHAP enhance trust and transparency. The solution minimizes manual configuration, reduces false positives, and provides clear insights for non-expert users. Scalable through containerization, the AI-WAF is ideal for small businesses and enterprises aiming to strengthen their web application security. By emphasizing ease of use, automation, and cost-efficiency, this work demonstrates the potential of AI to revolutionize web application protection for startups and SMEs.

## Tech Stack🚀:
__Frontend__ - Javascript
__Backend__ - Python
__Database__ - PostgreSQL

I want to use AI in the firewall in order to completely simplify the task and simply record and train models to detect any threats.

## Key Features
### Traffic Recording:
- Capture all incoming and outgoing HTTP/HTTPS requests and responses
- Log request metadata, such as IP addresses, headers, user agents, payloads, and timing
- Store labeled datasets for supervised learning, with labels such as "normal" or "threat" based on prior analysis or known vulnerabilities


## Model Training:
### Will use the recorded data to train AI models with the following capabilities:
- __Anomaly detection:__ unsupervised models like autoencoders or clustering algorithms like DBSCAN(​​density-based clustering non-parametric algorithm) to identify unusual patterns in traffic.
- __Threat classification:__ supervised models like Random Forest, Gradient Boosting (like library - XGBoost) or deep learning models such as transformers for classifying specific types of attacks (SQL injection, XSS, etc.(OWASP 10)).
- __Reinforcement Learning:__ will allow the system to adapt its rules dynamically based on real-world interactions and blocked threats.

## Threat Mitigation:
- automatically block or throttle suspicious requests based on model predictions.
- assign confidence scores to predictions to balance security and user experience (like blocking only high-confidence threats).


## Continuous Learning:
- integrate a feedback loop where security analysts can manually label false positives/negatives to improve model accuracy.
- use periodic retraining with the updated dataset to ensure the models adapt to new threat vectors.


## Explainability:
- provide clear reasoning for why a request was flagged as malicious (specific payload patterns, abnormal request frequency or unexpected headers).
- implement explainable AI techniques, such as LIME( local interpretable model-agnostic explanations) or SHAP(Shapley Additive Explanations) to ensure trust in the automated system.



## System Architecture
### Traffic Interception:
- Will deploy the AI-WAF inline as a reverse proxy to inspect and filter HTTP/HTTPs  traffic.
- Also, use tools like Nginx or HAProxy(will choose while implementation) to redirect traffic through the AI-WAF.


## AI Processing Pipeline:
- __Data Preprocessing:__ standardised request formats, tokenized payloads

- __Features:__
  - Request frequency
  - Payload entropy
  - Query structure
  - Header anomalies
- __Model Inference:__ use trained AI models to make real-time decisions on traffic.


## Logging & Feedback:
- Maintain a secure database for logs, labels, and model performance metrics.
- Allow administrators to review flagged traffic and provide corrections.


## Deployment & Scaling(final steps):
- Use containerized deployments (Docker) for horizontal scalability.
- Implement redundancy and failover mechanisms to ensure high availability.







# Unique Features of Your Custom AI-WAF for [!404respuestas](not404respuestas.netlify.app)
- __Simplicity & Adaptivity:__ Automates threat detection without requiring manual rule updates or configurations. + Continuously evolves to address new attack vectors as they emerge.
- __Efficiency:__ minimises false positives and false negatives with advanced models.
- __Scalability:__ handles large-scale traffic efficiently with real-time inference capabilities.
- __Cost Savings:__ reduces the need for extensive manual analysis and rule tuning.
- __Initial Dataset Creation:__ Use synthetic data and existing datasets (OWASP, Juice Shop logs) to bootstrap the training process.
- __Performance Overhead:__ optimised models for real-time inference using frameworks like TensorFlow 

