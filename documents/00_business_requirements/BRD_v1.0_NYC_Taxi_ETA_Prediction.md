# Business Requirements Document (BRD)

## NYC Taxi ETA Prediction Platform

---

**Document Information**

| Field               | Details                                             |
| ------------------- | --------------------------------------------------- |
| **Project Name**    | NYC Taxi Estimated Time of Arrival (ETA) Prediction |
| **Version**         | 1.0                                                 |
| **Date**            | November 19, 2025                                   |
| **Project Lead**    | Ravi Kumar Chavva                                   |
| **Faculty Advisor** | Prof. Dakshanamoorthi                               |
| **Team Members**    | Student 1 (TBD), Student 2 (TBD)                    |

---

## Executive Summary

This project aims to build an intelligent, end-to-end machine learning system that predicts **Estimated Time of Arrival (ETA)** for taxi trips in New York City. By leveraging historical trip data, weather patterns, and traffic conditions, the platform will demonstrate state-of-the-art ML model development and real-time inference capabilities so customers can get reliable trip duration estimates.

**Key Requirements:**

- Build predictive models to reliably estimate the time of arrival
- Develop a BI dashboard for stakeholders to analyze the data
- Build an agentic chatbot to answer ad-hoc queries for stakeholders

---

## Problem Statement

### Current Situation

Taxi passengers and dispatchers often lack accurate ETA predictions, leading to:

- Poor user experience and planning difficulties
- Inefficient fleet management
- Missed opportunities for route optimization

### Proposed Solution

Build a predictive analytics platform that:

1. Processes historical and real-time data
2. Trains ML models to predict trip duration
3. Serves predictions via REST API
4. Provides insights through interactive dashboards
5. Enables natural language queries via chatbot

### Why This Matters

- **For Passengers**: Better time management and arrival planning
- **For Operators**: Improved dispatch efficiency and customer satisfaction
- **For City Planners**: Data-driven insights into traffic patterns
- **For ML Engineers**: Showcase of production ML pipeline design

---

## Project Scope

### In Scope

#### 1. Data Engineering Pipeline

- Ingest historical NYC taxi trip data (2009-2025)
- Integrate weather and traffic data
- Build automated ETL pipeline using Apache Airflow
- Implement data quality validation
- Store processed data in Delta Lake

#### 2. Machine Learning Development

- Train predictive models for ETA prediction
- Implement experiment tracking using MLflow
- Develop feature engineering pipeline
- Deploy best performing model to production

#### 3. User Interfaces

- **ETA Prediction Form (Model Deployment)**: Web-based interface for users to input trip details and get real-time ETA predictions

  - Pickup and dropoff location selection
  - Date and time picker (Default: Now)
  - Display predicted ETA with confidence interval

- **BI Dashboard**: Analytics dashboard for stakeholders

  - Trip duration trends by time and location
  - Weather impact analysis
  - Model performance metrics
  - Historical data visualization

- **GenAI Chatbot**: Conversational interface using MCP

  - Natural language queries about taxi operations
  - Ad-hoc data exploration
  - Trigger predictions via chat
  - Explain model predictions

---

## Success Criteria

### Quantitative Metrics

| Metric                    | Target        | Measurement Method            |
| ------------------------- | ------------- | ----------------------------- |
| **Model Accuracy (RMSE)** | ≤ 3 minutes   | Validation dataset evaluation |
| **Model R² Score**        | ≥ 0.85        | Regression performance metric |
| **API Response Time**     | < 200ms (p95) | Load testing with Locust      |
| **Pipeline Success Rate** | ≥ 95%         | Airflow DAG monitoring        |
| **Code Coverage**         | ≥ 70%         | pytest + coverage.py          |
| **Data Quality Score**    | ≥ 90%         | Great Expectations validation |

### Qualitative Metrics

- Clean, well-documented codebase
- Reproducible ML experiments
- Clear architecture documentation
- Interactive and intuitive dashboard
- Functional chatbot with useful responses
- Professional GitHub repository presentation

---

## Stakeholders and Users

### Project Team

| Role                      | Name                  | Responsibilities                                    |
| ------------------------- | --------------------- | --------------------------------------------------- |
| **Project Lead**          | Ravi Kumar Chavva     | Overall architecture, ML pipeline, deployment       |
| **Faculty Advisor**       | Prof. Dakshanamoorthi | Guidance, best practices, industry standards review |
| **Student Contributor 1** | TBD                   | Data engineering, ETL pipeline development          |
| **Student Contributor 2** | TBD                   | ML model development, feature engineering           |

### Primary Audience

- **Hiring Managers & Recruiters**: Evaluating ML/Data Engineering skills
- **Technical Peers**: Code review and collaboration
- **Open Source Community**: Learning and contribution
- **Students & Educators**: Learning industrial ML project practices

### Use Cases

1. **Portfolio Showcase**

   - Demonstrate end-to-end ML pipeline design
   - Show proficiency in modern data stack
   - Highlight problem-solving approach

2. **Educational Resource**

   - Teaching material for ML pipeline development
   - Reference architecture for similar projects
   - Best practices demonstration

3. **Research & Analysis**

   - Urban mobility pattern analysis
   - Weather impact on transportation
   - Time-series forecasting applications

_Note: This is a living document and will be updated as the project evolves._
