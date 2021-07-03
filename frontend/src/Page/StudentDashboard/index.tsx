import React from "react";
import MyTopics from "./components/MyTopics";
import AllTopics from "./components/AllTopics";
import { Tabs } from "antd";
import styled from "@emotion/styled";
const { TabPane } = Tabs;

const Wrapper = styled.div`
  padding-top: 40px;
`;

const StudentDashboard = () => {
  return (
    <Wrapper>
      <Tabs type="card">
        <TabPane tab="All Topics" key="2">
          <AllTopics />
        </TabPane>
        <TabPane tab="My Topics" key="1">
          <MyTopics />
        </TabPane>
      </Tabs>
    </Wrapper>
  );
};
export default StudentDashboard;
