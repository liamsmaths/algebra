import React, { useEffect, useState } from "react";
import styled from "@emotion/styled";
import { Checkbox, Col, Form, Input, notification, Row, Typography, Button } from "antd";
import { useForm } from "antd/lib/form/Form";

// import ActionButton from "../../../components/ActionButton";
import logo from "../../../image/login.jpg";

const { Title, Text } = Typography;

const StyledLogoContainer = styled(Row)`
  margin-bottom: 1.5em;
`;

const StyledLogo = styled("img")`
  font-size: 1.5em;
  font-weight: 500;
`;

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
const StyledLink = styled("a")`
  color: #20a0da !important;
`;

function LoginForm(props: SignUpFormProps) {
  const [form] = useForm();
  const { setAnimation, animation } = props;

  useEffect(() => {}, []);
  return (
    <StyledLoginForm>
      <div>
        <StyledLogoContainer>
          {/* <Col>
            <StyledLogo src={logo} />
          </Col> */}
        </StyledLogoContainer>
        <Title style={{ fontSize: "1.5em" }}>Log In</Title>
        <Text style={{ fontSize: "15px", marginBottom: "0.9em", display: "block" }}>
          Log in with your data that you entered during registration.
        </Text>
        <StyledForm form={form} layout="vertical" size="large" hideRequiredMark>
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
          {/* <Form.Item name="rememberMe" valuePropName="checked" noStyle>
            <StyledCheckbox>Keep me logged in</StyledCheckbox>
          </Form.Item> */}
          <Row justify="center" align="middle">
            <Col span={24}>
              {/* <ActionButton
                size="large"
                style={{
                  width: "100%",
                  background: "169af4",
                  borderRadius: "8px",
                  fontSize: "1em",
                  border: " 1px solid #30a3e2a1",
                }}
                url="/api/v1.1/Account/SignIn"
                onSuccess={(response: any) => {
                  notification.open({
                    message: "Success",
                    description: "You have successfully logged in",
                    duration: 2,
                  });
                  const currentUser = form.getFieldsValue();
                  if (currentUser.rememberMe === true) {
                    localStorage.setItem("loggedUsername", currentUser.email);
                    localStorage.setItem("loggedPassword", currentUser.password);
                  }
                  if (currentUser.rememberMe === undefined) {
                    localStorage.setItem("loggedUsername", "");
                    localStorage.setItem("loggedPassword", "");
                  }
                  localStorage.setItem("current", response.data.data.userId);
                  localStorage.setItem("token", response.data.data.token);
                  localStorage.setItem("loggedIn", currentUser.rememberMe);

                  const user: any = jwt(response.data.data.token);
                  const roleFunction = (role: any) => {
                    switch (role) {
                      case "Super Admin":
                        return "superAdmin";
                      case "Mentor Admin":
                        return "mentorAdmin";
                      case "Candidate Admin":
                        return "candidateAdmin";
                      case "Account":
                        return "account";
                      default:
                        return "superAdmin";
                    }
                  };
                  let role = roleFunction(user.roles);
                  history.push(routes[role].navRoutes[0].path);
                }}
                onError={() => {
                  notification.open({
                    message: "Error",
                    description: "Email Or Password is incorrect",
                    placement: "topLeft",
                    duration: 2,
                  });
                }}
                onSubmit={({ setFormData, setIsReady }: any) => {
                  form
                    .validateFields()
                    .then((values) => {
                      const { email, password } = values;
                      setFormData({
                        userName: email,
                        password,
                        rememberMe: true,
                      });
                      setIsReady(true);
                    })
                    .catch((errorInfo) => {
                      console.log(errorInfo.message);
                      setIsReady(false);
                    });
                }}
              >
                Log In
              </ActionButton> */}
              <Button type="primary">Log In</Button>
            </Col>
          </Row>
          <Row
            justify="center"
            align="middle"
            style={{ flexDirection: "column", margin: "25px 0" }}
          >
            {/* <Col>
              <StyledLink onClick={() => setAnimation(!animation)}> Forgot Pasword?</StyledLink>
            </Col> */}
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
