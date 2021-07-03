import React from "react";
import MyTopics from "./components/MyTopics";
import AllTopics from "./components/AllTopics";
import { Tabs } from "antd";
const { TabPane } = Tabs;

const StudentDashboard = () => {
  return (
    <React.Fragment>
      <Tabs type="card">
        <TabPane tab="All Topics" key="2">
          <AllTopics />
        </TabPane>
        <TabPane tab="My Topics" key="1">
          <MyTopics />
        </TabPane>
      </Tabs>
    </React.Fragment>
  );
};
export default StudentDashboard;
