CREATE DATABASE IF NOT EXISTS rpms_db;
USE rpms_db;

CREATE TABLE IF NOT EXISTS candidates (
  candidate_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(150) NOT NULL UNIQUE,
  mobile VARCHAR(10) NOT NULL UNIQUE,
  qualification VARCHAR(100) NOT NULL,
  percentage DECIMAL(5,2) NOT NULL,
  passing_year YEAR NOT NULL,
  technology VARCHAR(80) NOT NULL,
  skills TEXT,
  backlogs INT NOT NULL DEFAULT 0,
  active BOOLEAN NOT NULL DEFAULT TRUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CHECK (percentage BETWEEN 0 AND 100),
  CHECK (backlogs >= 0)
);

CREATE TABLE IF NOT EXISTS companies (
  company_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(150) NOT NULL,
  industry VARCHAR(100),
  location VARCHAR(150),
  contact_email VARCHAR(150),
  phone VARCHAR(20),
  active BOOLEAN DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS jobs (
  job_id INT AUTO_INCREMENT PRIMARY KEY,
  company_id INT NOT NULL,
  title VARCHAR(150) NOT NULL,
  technology VARCHAR(80) NOT NULL,
  openings INT NOT NULL,
  location VARCHAR(150),
  package_lpa DECIMAL(8,2),
  min_percentage DECIMAL(5,2) NOT NULL,
  passing_year YEAR NOT NULL,
  max_backlogs INT NOT NULL DEFAULT 0,
  deadline DATE NOT NULL,
  status ENUM('OPEN','CLOSED') DEFAULT 'OPEN',
  FOREIGN KEY (company_id) REFERENCES companies(company_id),
  CHECK (openings > 0),
  CHECK (min_percentage BETWEEN 0 AND 100)
);

CREATE TABLE IF NOT EXISTS applications (
  application_id INT AUTO_INCREMENT PRIMARY KEY,
  candidate_id INT NOT NULL,
  job_id INT NOT NULL,
  status ENUM('APPLIED','SHORTLISTED','INTERVIEW','SELECTED','OFFERED','JOINED','REJECTED') DEFAULT 'APPLIED',
  applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UNIQUE KEY uq_candidate_job(candidate_id,job_id),
  FOREIGN KEY (candidate_id) REFERENCES candidates(candidate_id),
  FOREIGN KEY (job_id) REFERENCES jobs(job_id)
);

CREATE TABLE IF NOT EXISTS interviews (
  interview_id INT AUTO_INCREMENT PRIMARY KEY,
  application_id INT NOT NULL,
  round_name VARCHAR(80) NOT NULL,
  interview_date DATETIME NOT NULL,
  mode VARCHAR(30),
  interviewer VARCHAR(100),
  technical_rating DECIMAL(3,1),
  communication_rating DECIMAL(3,1),
  remarks TEXT,
  result VARCHAR(30),
  FOREIGN KEY (application_id) REFERENCES applications(application_id)
);

CREATE TABLE IF NOT EXISTS offers (
  offer_id INT AUTO_INCREMENT PRIMARY KEY,
  application_id INT NOT NULL,
  designation VARCHAR(100) NOT NULL,
  package_lpa DECIMAL(8,2) NOT NULL,
  offer_date DATE NOT NULL,
  joining_date DATE,
  offer_status VARCHAR(30) DEFAULT 'PENDING',
  FOREIGN KEY (application_id) REFERENCES applications(application_id)
);

CREATE TABLE IF NOT EXISTS placements (
  placement_id INT AUTO_INCREMENT PRIMARY KEY,
  application_id INT NOT NULL UNIQUE,
  company_id INT NOT NULL,
  designation VARCHAR(100) NOT NULL,
  final_package DECIMAL(8,2) NOT NULL,
  actual_joining_date DATE,
  joining_status VARCHAR(30) DEFAULT 'PENDING',
  FOREIGN KEY (application_id) REFERENCES applications(application_id),
  FOREIGN KEY (company_id) REFERENCES companies(company_id)
);
