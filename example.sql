-- Blood Donation Management System Database Schema
-- This SQL code creates the necessary tables for the PROJ.py application

-- Users table for login
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

-- Insert default user (from PROJ.py hardcoded values)
INSERT OR IGNORE INTO users (username, password) VALUES ('johnsmith', '12345');

-- Donors table
CREATE TABLE IF NOT EXISTS donors (
    d_id INTEGER PRIMARY KEY,
    dname TEXT NOT NULL,
    age INTEGER NOT NULL,
    gender TEXT NOT NULL,
    b_grp TEXT NOT NULL CHECK (b_grp IN ('A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-')),
    ph_no TEXT NOT NULL CHECK (LENGTH(ph_no) = 10),
    H_issue TEXT NOT NULL
);

-- Records table for donations
CREATE TABLE IF NOT EXISTS records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    d_id INTEGER NOT NULL,
    dname TEXT NOT NULL,
    Donation_Date TEXT NOT NULL,
    FOREIGN KEY (d_id) REFERENCES donors(d_id)
);

-- Sample data (optional, for testing)
INSERT OR IGNORE INTO donors (d_id, dname, age, gender, b_grp, ph_no, H_issue) VALUES
(1, 'Alice Johnson', 25, 'Female', 'O+', '1234567890', 'N'),
(2, 'Bob Smith', 30, 'Male', 'A-', '0987654321', 'N');

INSERT OR IGNORE INTO records (d_id, dname, Donation_Date) VALUES
(1, 'Alice Johnson', '2023-10-01'),
(2, 'Bob Smith', '2023-10-15');