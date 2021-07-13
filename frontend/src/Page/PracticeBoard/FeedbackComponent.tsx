import React, { useState } from "react";
import { Input, Button } from "antd";
import styled from "@emotion/styled";
import jwt from "jwt-decode";
import axios from "axios";

const { TextArea } = Input;

const StyledButton = styled(Button)`
  background: #6d60b0;
  color: white;
  border-radius: 5px;
  height: 40px;
  &:hover,
  &:focus {
    background: #6d60b0;
    color: white;
  }
  border: none;
`;

const FeedbackComponent = (props: any) => {
  const { topicId, setIsFeedback } = props;
  const token: any = localStorage.getItem("token");
  const user: any = jwt(token);
  const [feedbackMessage, setFeedbackMessage] = useState("");

  const handleFeedbackMessage = (e: any) => {
    setFeedbackMessage(e.target.value);
  };
  const handleFeedbackSubmit = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:8000/api/feedback", {
        student_id: user.id,
        topic_id: topicId,
        message: feedbackMessage,
      });
      setIsFeedback(false);
    } catch (e) {}
  };

  return (
    <React.Fragment>
      <TextArea rows={5} style={{ marginTop: "15px" }} onChange={handleFeedbackMessage} />
      <StyledButton style={{ marginTop: "15px" }} onClick={handleFeedbackSubmit}>
        Submit
      </StyledButton>
    </React.Fragment>
  );
};
export default FeedbackComponent;
