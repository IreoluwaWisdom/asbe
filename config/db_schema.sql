-- Drop the database if it exists
DROP DATABASE IF EXISTS attendance_system;

-- Create the database and connect to it
CREATE DATABASE attendance_system;
\c attendance_system;

-- Drop the table if it exists
DROP TABLE IF EXISTS users CASCADE;

-- Create the users table
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  department VARCHAR(100),
  email VARCHAR(255) UNIQUE NOT NULL,
  facialScan BYTEA, -- Store the vector embedding as binary data
  faculty VARCHAR(100),
  fullName VARCHAR(100),
  gender VARCHAR(10),
  matricNumber VARCHAR(50) UNIQUE NOT NULL,
  otp VARCHAR(10),
  otp_expires_at TIMESTAMP, -- Store OTP expiration time
  password VARCHAR(255) NOT NULL, -- Store hashed passwords
  is_verified BOOLEAN DEFAULT FALSE, -- Indicates if the user has confirmed their OTP
  role VARCHAR(20) DEFAULT 'user', -- User role (e.g., user, admin)
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  last_login TIMESTAMP
);

-- Trigger function to update updated_at column on row update
CREATE FUNCTION update_updated_at_column() 
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger to call the update function on user table update
CREATE TRIGGER trigger_update_users_updated_at
BEFORE UPDATE ON users
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

-- Indexes for faster lookups
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_matricNumber ON users(matricNumber);
