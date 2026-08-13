"""Test cases for the Mergington High School API activities endpoints

This module tests the following endpoints:
- GET /activities - Retrieve all activities
- POST /activities/{activity_name}/signup - Sign up a student for an activity
- DELETE /activities/{activity_name}/participants/{email} - Remove a student from an activity
"""

import pytest


class TestGetActivities:
    """Tests for GET /activities endpoint"""
    
    def test_get_activities(self, client, reset_activities):
        """Arrange-Act-Assert: Retrieve all activities successfully
        
        Arrange: Test client is ready
        Act: Send GET request to /activities
        Assert: Response status is 200 and contains all 9 activities
        """
        # Arrange
        # (client and reset_activities fixtures set up the initial state)
        
        # Act
        response = client.get("/activities")
        
        # Assert
        assert response.status_code == 200
        activities_data = response.json()
        assert len(activities_data) == 9
        assert "Chess Club" in activities_data
        assert "Programming Class" in activities_data
        assert "Gym Class" in activities_data
        assert "Basketball Team" in activities_data
        assert "Tennis Club" in activities_data
        assert "Drama Club" in activities_data
        assert "Art Studio" in activities_data
        assert "Debate Team" in activities_data
        assert "Science Club" in activities_data


class TestSignupForActivity:
    """Tests for POST /activities/{activity_name}/signup endpoint"""
    
    def test_signup_for_activity(self, client, reset_activities):
        """Arrange-Act-Assert: Sign up a new student for an activity successfully
        
        Arrange: Choose an activity and a new student email
        Act: Send POST request to sign up the student
        Assert: Response indicates success and student is added to participants
        """
        # Arrange
        activity_name = "Chess Club"
        new_student_email = "newstudent@mergington.edu"
        
        # Act
        response = client.post(
            f"/activities/{activity_name}/signup",
            params={"email": new_student_email}
        )
        
        # Assert
        assert response.status_code == 200
        assert response.json()["message"] == f"Signed up {new_student_email} for {activity_name}"
        
        # Verify student was added to the activity's participants
        activities_response = client.get("/activities")
        activities_data = activities_response.json()
        assert new_student_email in activities_data[activity_name]["participants"]


class TestRemoveParticipant:
    """Tests for DELETE /activities/{activity_name}/participants/{email} endpoint"""
    
    def test_remove_participant(self, client, reset_activities):
        """Arrange-Act-Assert: Remove a student from an activity successfully
        
        Arrange: Choose an activity and an existing participant
        Act: Send DELETE request to remove the participant
        Assert: Response indicates success and student is removed from participants
        """
        # Arrange
        activity_name = "Chess Club"
        participant_email = "michael@mergington.edu"  # Existing participant
        
        # Act
        response = client.delete(
            f"/activities/{activity_name}/participants/{participant_email}"
        )
        
        # Assert
        assert response.status_code == 200
        assert response.json()["message"] == f"Removed {participant_email} from {activity_name}"
        
        # Verify student was removed from the activity's participants
        activities_response = client.get("/activities")
        activities_data = activities_response.json()
        assert participant_email not in activities_data[activity_name]["participants"]
