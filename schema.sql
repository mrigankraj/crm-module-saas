-- Users table to store client information
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    company_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    contact_person VARCHAR(255),
    phone VARCHAR(20),
    industry VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    onboarding_status VARCHAR(50) DEFAULT 'pending',
    subscription_tier VARCHAR(50) DEFAULT 'basic'
);

-- Interactions table to track all client communications
CREATE TABLE interactions (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    type VARCHAR(50) NOT NULL,  -- email, call, meeting, etc.
    subject VARCHAR(255),
    content TEXT,
    status VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    scheduled_at TIMESTAMP,
    completed_at TIMESTAMP
);

-- Tasks table for tracking onboarding and general tasks
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(50) DEFAULT 'pending',
    priority VARCHAR(20) DEFAULT 'medium',
    due_date TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP
);

-- Analytics table for tracking user engagement
CREATE TABLE analytics (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    event_type VARCHAR(100) NOT NULL,
    event_data JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Communication preferences table
CREATE TABLE communication_preferences (
    user_id INTEGER PRIMARY KEY REFERENCES users(id),
    email_frequency VARCHAR(50) DEFAULT 'weekly',
    preferred_contact_method VARCHAR(50) DEFAULT 'email',
    newsletter_subscription BOOLEAN DEFAULT true,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
