import React from "react";
import styled from "@emotion/styled";
import Text from "antd/lib/typography/Text";
import { createFromIconfontCN } from "@ant-design/icons";
import { Popover, Button } from "antd";
import { useHistory } from "react-router-dom";
import jwt from "jwt-decode";

const IconFont = createFromIconfontCN({
  scriptUrl: "//at.alicdn.com/t/font_2643792_vtsize76u7.js",
});

const Wrapper = styled("div")`
  padding: 18px 12px 0px 12px;
  display: flex;
  justify-content: space-between;
  align-items: center;
`;
const DetailsWrapper = styled("div")`
  display: flex;
  align-items: center;
  gap: 15px;
`;

const HeaderComponent = () => {
  const history = useHistory();
  const token: any = localStorage.getItem("token");
  const user: any = jwt(token);
  const handleLogOut = () => {
    localStorage.removeItem("token");
    history.push("/");
  };
  return (
    <Wrapper>
      <Text
        style={{ fontSize: "24px", color: "white", textTransform: "uppercase", letterSpacing: 2 }}
      >
        Algebra Guide
      </Text>
      <DetailsWrapper>
        <Text style={{ fontSize: "20px", color: "white" }}>{user.name}</Text>
        <Popover
          placement="bottom"
          title=""
          content={
            <div onClick={handleLogOut} style={{ cursor: "pointer" }}>
              Logout
            </div>
          }
          trigger="click"
        >
          <IconFont type="icon-setting" style={{ fontSize: "20px", color: "white" }} />
        </Popover>
      </DetailsWrapper>
    </Wrapper>
  );
};
export default HeaderComponent;
