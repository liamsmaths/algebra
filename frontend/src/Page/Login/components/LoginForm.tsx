import React, { useEffect, useState } from "react";
import styled from "@emotion/styled";
import { Checkbox, Col, Form, Input, notification, Row, Typography, Button } from "antd";
import { useForm } from "antd/lib/form/Form";
import axios from "axios";
import logo from "../../../image/login.jpg";
import { useHistory } from "react-router-dom";

const { Title, Text } = Typography;

const StyledLoginForm = styled(Col)`
  box-shadow: -3px 18px 35px rgba(0, 0, 0, 0.12);
  z-index: 5;
  padding: 2em 5em 1px 4.5em;
  @media only screen and (max-width: 1024px) {
    padding: 40px 40px 20px 40px;
  }
  background: #f2faff;
  min-height: 84vh;
`;
const StyledInput = styled(Input)`
  border-radius: 5px;
  :active,
  :focus {
    border-color: #30a3e2a1;
    outline: none;
  }
`;

const StyledPassword = styled(Input.Password)`
  border-radius: 5px;
  :active,
  :focus {
    border-color: #30a3e2a1;
    outline: none;
  }
`;

const StyledForm = styled(Form)`
  height: 100%;
  .ant-form-item {
    margin-bottom: 20px;
  }
  .ant-form-item-label {
    padding: 0;
    font-size: 0.8em;
  }
`;
const StyledCheckbox = styled(Checkbox)`
  margin: 1em 0 1.5em;

  .ant-checkbox-inner {
    border-color: #20a0da;
  }
  .ant-checkbox-checked {
    .ant-checkbox-inner {
      border-color: #20a0da;
      background-color: #20a0da;
    }
  }
`;

function LoginForm(props: SignUpFormProps) {
  const [form] = useForm();
  const history = useHistory();
  const handleLogin = async (values: any) => {
    try {
      const response = await axios.post("http://127.0.0.1:8000/api/login", {
        email: values.email,
        password: values.password,
      });
      history.push("/home");
      notification.open({
        message: "Log In Success",
        description: "You have successfully logged in",
        duration: 2,
      });
    } catch (e) {
      notification.open({
        message: "Log In Failed",
        description: "Incorrect email or password",
        duration: 2,
      });
    }
  };

  useEffect(() => {}, []);
  return (
    <StyledLoginForm>
      <div>
        <Title style={{ fontSize: "1.5em" }}>Log In</Title>
        <Text style={{ fontSize: "15px", marginBottom: "0.9em", display: "block" }}>
          Log in with your data that you entered during registration.
        </Text>
        <StyledForm
          form={form}
          layout="vertical"
          size="large"
          hideRequiredMark
          onFinish={handleLogin}
        >
          <Form.Item
            label="Username"
            name="email"
            rules={[{ required: true, message: "Please enter your username!" }]}
          >
            <StyledInput placeholder="enter your username" />
          </Form.Item>
          <Form.Item
            label="Password"
            name="password"
            rules={[{ required: true, message: "Please enter your Password!" }]}
          >
            <StyledPassword type="password" placeholder="enter your password" />
          </Form.Item>

          <Row justify="center" align="middle">
            <Col span={24}>
              <Button htmlType="submit" style={{ background: "#6d60b0", color: "white" }}>
                Log In
              </Button>
            </Col>
          </Row>
        </StyledForm>
      </div>
    </StyledLoginForm>
  );
}

type SignUpFormProps = {
  setAnimation: any;
  animation: boolean;
};

export default LoginForm;
