import { Breadcrumb, Typography } from "antd";
import { useMemo } from "react";
import { useMatches, useNavigate } from "react-router-dom";
import React from 'react';

function BreadcrumbButton({ name }: { name: string }) {
  return <Typography style={{ cursor: "pointer" }}>{name}</Typography>;
}

export default function PathBreadcrumbs() {
  const matches = useMatches();
  const navigate = useNavigate();

  const capitalize = (s: string) =>
    s
      .split("-")
      .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
      .join(" ");

  const breadcrumbItems = useMemo(() => {
    const pathname = matches[matches.length - 1]?.pathname || "";
    const pathSegments = pathname.split("/").filter(Boolean);

    return pathSegments.map((segment, index) => {
      const pathToSegment = "/" + pathSegments.slice(0, index + 1).join("/");
      const name = segment.split("-").map(capitalize).join(" ");

      return {
        title: <BreadcrumbButton name={name} />,
        onClick: () => navigate(pathToSegment),
      };
    });
  }, [matches, navigate]);

  return (
    <Breadcrumb
      style={{ margin: "16px 0" }}
      items={breadcrumbItems}
    />
  )
}